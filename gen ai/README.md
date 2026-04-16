# Gen AI - NGT Studio

Gen AI - NGT Studio is a desktop application that provides a graphical user interface (GUI) for generating AI images using Stable Diffusion. It uses the `CompVis/stable-diffusion-v1-4` model to transform text prompts into stunning visual art.

## Features

- **Secure Login**: Access control with a dedicated authentication screen.
- **Prompt-to-Image**: Generate high-quality images from simple text descriptions.
- **Live Preview**: See your generated image directly within the application.
- **Auto-Save**: Automatically saves generated images as `generatedimage.png`.
- **Easy Access**: One-click button to open the generated image in the default system viewer.

## Screenshots

*(Run the application to see the futuristic dark-themed login and the clean generation interface!)*

## Prerequisites

Before running the application, ensure you have Python installed and a compatible GPU (CUDA) for faster generation, though it also supports CPU.

## Installation

1. Clone the repository or download the files.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Execute the main script:

```bash
python gen.py
```

### Credentials

- **Username**: `admin`
- **Password**: `1234`

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: GUI framework for the desktop interface.
- **Diffusers**: Library for state-of-the-art pretrained diffusion models.
- **PyTorch**: Deep learning framework.
- **Pillow**: Image processing library.

## License

This project is for educational and creative purposes.
