# Conversphere: Interview Simulation App

## Project Overview
This project provides an interactive platform for users to simulate interviews and improve their skills. It offers two primary features:

- **Mock Interview Sessions:** Users participate in real-time interviews with dynamic question prompts.
- **Skill Analysis Reports: ** Provides detailed feedback on facial expressions, eye contact, and speech clarity.

This tool is designed to help job seekers prepare effectively for professional interviews.

## Models
The application leverages OpenCV for real-time video analysis and Flask to build a web-based interface. Custom algorithms evaluate non-verbal communication, offering actionable insights for users to enhance their performance.

## How it Works
1. Users access the app via a browser.
2. The webcam records interactions during mock interviews.
3. OpenCV processes the video feed to analyze body language and facial expressions.
4. Results and feedback are presented in real-time or as post-session reports.

## Steps to Execute
1. Download the entire project zip file or clone the repository.
   ```bash
   git clone https://github.com/Vaibh2/Conversphere  
   ```
2. Download the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook file to initialize and test the YOLOv5 model:
   ```bash
   python app.py  
   ```
4. Open the application in your browser.

5. Simulate a mock interview session and review the feedback.

## Requirements
Ensure the following dependencies are installed:

- Python 3.x
- Flask
- OpenCV
- NumPy
- SpeechRecognition
- Matplotlib

You can install them using:
```bash
pip install -r requirements.txt
```

## Future Improvements
- Integrate AI-driven feedback for tailored suggestions.
- Expand language support for interviews.
- Create a mobile-responsive version.

## Acknowledgments
Special thanks to the OpenCV and Flask communities for their open-source resources, enabling this project.



---
For any issues or contributions, feel free to open an issue or submit a pull request.

