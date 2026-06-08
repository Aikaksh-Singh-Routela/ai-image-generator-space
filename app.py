import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io
import time

st.set_page_config(page_title="AI Image Generator", page_icon="🎨")

st.title("🎨 AI Image Generator")
st.markdown("Generate images from text descriptions")

@st.cache_resource
def load_model():
    with st.spinner("🔄 Loading AI model... (2-3 minutes on first run)"):
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32,
            safety_checker=None
        )
        pipe = pipe.to("cpu")
        return pipe

prompt = st.text_area("Enter your prompt:", "cute golden retriever puppy")

if st.button("Generate Image"):
    with st.spinner("Generating... (1-2 minutes)"):
        pipe = load_model()
        image = pipe(prompt, num_inference_steps=25).images[0]
        st.image(image, caption=prompt)
        
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        st.download_button("Download Image", buf.getvalue(), "image.png", "image/png")