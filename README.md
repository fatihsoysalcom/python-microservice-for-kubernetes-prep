# Python Microservice for Kubernetes Prep

This example provides a simple Python Flask microservice, demonstrating key patterns for applications intended for containerization and deployment on Kubernetes. It shows how to externalize configuration using environment variables and includes a health check endpoint, both vital for robust Kubernetes deployments and effective scaling.

## Language

`python`

## How to Run

1. Ensure Python 3 and pip are installed. 
2. Install Flask: `pip install Flask`. 
3. Run the application: `python main.py` or `PORT=8080 APP_NAME='MyBackendService' python main.py`. 
4. Access it in your browser at `http://localhost:5000/` (or `http://localhost:8080/`).

## Original Article

This example accompanies the Turkish article: [DigitalOcean eBook: Kubernetes for Full-Stack Developers - Kapsamlı Bir Bakış](https://fatihsoysal.com/blog/?p=42150).

## License

MIT — see [LICENSE](LICENSE).
