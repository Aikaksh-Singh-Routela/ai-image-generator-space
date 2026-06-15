# 🎨 AI Image Generator - Stable Diffusion

**Built by Aikaksh Singh Routela**

Generate stunning images from text descriptions using Stable Diffusion. This app runs on Hugging Face Spaces with zero configuration.

## 🚀 Live Demo
[Click here to try the live app](https://huggingface.co/spaces/Aikaksh-Singh-Routela/ai-image-generator-space)

## 📂 GitHub Repository
[https://github.com/Aikaksh-Singh-Routela/ai-image-generator-space](https://github.com/Aikaksh-Singh-Routela/ai-image-generator-space)

## 🛠️ Tech Stack
- **Model**: Stable Diffusion 1.5 (runwayml/stable-diffusion-v1-5)
- **Framework**: 🧨 Diffusers
- **Backend**: PyTorch
- **UI**: Gradio
- **Deployment**: Hugging Face Spaces (Docker)

## ✨ Features
- 🖼️ Generate high-quality images from text prompts
- ⚙️ Adjustable quality steps (10-50)
- 🎨 Creativity control (guidance scale 1-15)
- 📥 Download generated images
- 🆓 Completely free to use

## 📝 Example Prompts
| Prompt | Style |
|--------|-------|
| "cute golden retriever puppy" | Animals |
| "beautiful sunset over mountains" | Landscape |
| "futuristic cyberpunk city" | Sci-fi |
| "close-up of a rose with dew" | Nature |

## 🚀 Local Setup

```bash
# Clone the repository
git clone https://github.com/Aikaksh-Singh-Routela/ai-image-generator-space.git
cd ai-image-generator-space

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
🎯 How It Works
Enter a text description of the image you want

Adjust settings for quality and creativity

Click "Generate Image"

Stable Diffusion creates a unique image from your prompt

Download the result

📁 Project Structure
text
ai-image-generator-space/
├── app.py              # Gradio application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
└── README.md          # Documentation
👨‍💻 Author
Aikaksh Singh Routela

📎 Related Projects
AI Assistant - Web Search & Math

RAG Chatbot - PDF Q&A

