# Leftover Vision

Leftover Vision is a web application designed to identify images of food waste. The idea of this application originated from my time as a Sustainability Intern at Boston University Dining Services. I wanted to leverage machine learning and image classification to classify incoming plates of food waste to help determine the most wasted food at the dining hall.

I attempted to use TensorFlow to build a custom model but there's not much data pertaining to food waste available. So I decided to use AWS Rekognition - an out of the box image classification service. It works well in a lot of instances, but there's always the cases where it misidenitifies something entirely.

I was able to find [Foodvisor](https://www.foodvisor.io/en/vision/#pricing) which is a food specific image classification service. It's a much better solution - the model will only classify items as food, as opposed to Rekognition, which does not have those guardrails in place. I hope to implement this in the future.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)

## Installation

### Prerequisites

- Python 3.0+
- Pip

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/mmeah16/leftover-vision.git
   ```
2. Navigate to the project directory:
   ```bash
   cd leftover-vision
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Configuring the Database (PostgreSQL with Docker)

#### Steps

1. **Pull the PostgreSQL Docker Image**
   ```bash
   docker pull postgres
   ```
2. **Run the Docker Container**

   ```bash
   docker run --name <database-name> \
   -e POSTGRES_PASSWORD=<database-password> \
   -p 5432:5432 \
   -d postgres
   ```

   - `<database-name>`: The name you want to give your container.
   - `<database-password>`: The password for the `postgres` user.
   - `-p 5432:5432`: Exposes PostgreSQL port `5432` on your local machine.

3. **Connect to the Database Using PGAdmin or any SQL Client**

   Use the following details to connect:

   - **Host:** `localhost`
   - **Port:** `5432`
   - **Maintenance Database:** `postgres`
   - **Username:** `postgres`
   - **Password:** `Password set up during step 2`

### Running the Application

#### Steps

1. **Build the Docker Image**

   ```bash
   docker build --tag leftover-vision .
   ```

2. **Run the Docker Image**

   ```bash
   sudo docker run --name leftover-vision -p 5001:5001 leftover-vision
   ```

3. **Test the Image**

   Visit [http://127.0.0.1:5001/](http://127.0.0.1:5001/) to verify the application is working properly.

#### Steps (For Running After CI/CD Workflow)

1. **Pull the Docker Image**

   ```bash
   docker pull --platform linux/amd64 <docker_hub_username>/leftover-vision
   ```

2. **Run the Docker Image**

   ```bash
   sudo docker run --platform linux/amd64 --name leftover-vision -p 5001:5001 <docker_hub_username>/leftover-vision:latest
   ```

3. **Test the Image**

   Visit [http://127.0.0.1:5001/](http://127.0.0.1:5001/) to verify the application is working properly.

## Tech Stack

### Backend

- **Languages**:

  - Python

- **Frameworks**:

  - Flask

- **Database**:
  - PostgreSQL

### DevOps/Infrastructure

- **Cloud**:

  - AWS Elastic Container Service (ECS)

- **CI/CD**:

  - GitHub Actions

- **Containerization**:
  - Docker

### Tools & Other Technologies

- **Authentication & Authorization**:

  - Flask-Login

- **Image Classification**:

  - AWS Rekognition (current state)

- **Version Control**:
  - Git
  - GitHub

## License

This project is licensed under the MIT License - see [MIT LICENSE](https://opensource.org/license/mit) for more details.

Flask is licensed under the BSD-3 License. See [Flask's License](https://palletsprojects.com/p/flask/#license) for more information.
