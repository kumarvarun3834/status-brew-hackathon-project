# status-brew-hackathon-project


# **Empowering Education Through Technology**

## **Project Overview**
This project aims to create a Telegram bot and a companion website to help university students access and share study materials like previous years' question papers (PYQs), notes, and textbooks. The platform is designed to be intuitive and easy to use, with features like file categorization, search filters, and a Google Drive-like interface for file management.

## **Key Features**
- **File Upload/Download via Telegram Bot**: Users can easily upload and download study materials directly through the bot.
- **File Categorization**: Files are organized by semester, year, subject, etc., making it easy to find what you need.
- **Google Drive-like Interface**: The website offers a familiar and user-friendly interface for managing files.
- **Community Support**: The platform encourages students to share resources, fostering a collaborative learning environment.

## **Technology Stack**
- **Python**: Backend logic and file management.
- **Django**: Framework used to develop the website.
- **HTML/CSS/Bootstrap**: Frontend development for the website, ensuring a responsive and user-friendly design.
- **CSV**: Used for handling file data.
- **Telegram API**: For bot development and user interaction.

## **Installation & Setup**
### Prerequisites
- Python 3.x
- Django
- Telegram Bot API Token
- Other Python libraries as specified in `requirements.txt`

### Steps
1. **Clone the Repository**:  
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Django**:  
   Configure the Django settings, run migrations, and create a superuser.
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run the Development Server**:  
   ```bash
   python manage.py runserver
   ```

5. **Telegram Bot Setup**:  
   Add your Telegram Bot API Token to the environment variables or directly into the bot configuration.

6. **Access the Application**:  
   Visit `http://127.0.0.1:8000/` to access the website.

## **Usage**
- **Telegram Bot**: Start the bot and follow the on-screen instructions to upload, download, and manage files.
- **Website**: Use the Google Drive-like interface to search, filter, and manage your study materials.

## **Team Members**
- Varun Kumar
- Tushar Dhingra
- Anshika Gupta
- Simran Juneja

## **Future Scope**
- Expand the platform to include more courses and departments.
- Introduce features like user profiles, community engagement tools, and notifications.

## **Known Issues & Limitations**
- Potential risks include legal concerns over sharing copyrighted materials and Telegram's availability in certain regions.

## **Contact**
For any questions or issues, please contact [your email/contact info].

