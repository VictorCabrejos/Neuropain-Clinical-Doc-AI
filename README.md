
# Neuropain Clinical Doc AI

**Automated Clinical Documentation Generator using Generative AI**
*Created by Victor Manuel Cabrejos Jr.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/victorcabrejos/)
[![Facebook](https://img.shields.io/badge/Facebook-Follow-blue)](https://www.facebook.com/pythonfordatascience)

---
**Project Context**

This project originated from a presentation delivered for the Master's Program in Informatics with a Specialization in Software Engineering at Universidad Ricardo Palma. That initial phase demonstrated how to automate software testing using Python and Generative AI. You can still find the slides for that presentation here: [Grossinger LLM Presentation](https://www.dropbox.com/scl/fi/3wj1bk97gxqvnfyswa4kn/grossinger_llm_pres.pdf?rlkey=35gcbmw7duijo9ie3txw4ukrx&st=b2zb0wx8&dl=0).

**Phase 2** of the project was presented at the **1st International Congress on Data Science and Artificial Intelligence**, hosted by Universidad Ricardo Palma and its Instituto de Datos e Inteligencia Artificial (IDIA). This phase expands the initial work by implementing **Retrieval-Augmented Generation (RAG)** to improve accuracy and mitigate hallucinations in AI-powered medical documentation. Slides from this phase can be found here: [Neuropain RAG Presentation](ADD_SLIDES_LINK_HERE).

---

## 📜 Overview

**Neuropain Clinical Doc AI** is a cutting-edge application designed to automate the generation of clinical documentation using Generative AI models. Specifically tailored for the needs of **Grossinger Neuropain Specialists**, this project leverages the power of the GPT-4o mini model, integrated with a Flask backend, to streamline the creation of personalized medical reports.

With the integration of **RAG** techniques in Phase 2, the project ensures greater accuracy by referencing external data sources, minimizing the risks of hallucinations, and enabling support for complex and diverse medical documentation requirements.

---

## 🚀 Features

- **Automated Report Generation**: Quickly generate detailed and personalized medical reports based on patient data.
- **RAG-Enhanced Accuracy**: Uses Retrieval-Augmented Generation to incorporate reliable external data and reduce hallucinations.
- **Consistency & Accuracy**: Ensures that all documentation follows a standardized format, reducing the likelihood of errors.
- **Scalable Architecture**: Built using Flask, making it easy to deploy and scale in a variety of environments.
- **Customizable Templates**: Easily adjust the report templates to match specific clinical needs.

---

## ⚙️ Tech Stack

- **Backend**: Flask (Python)
- **AI Model**: GPT-4o mini, integrated via LangChain
- **Enhanced with RAG**: Retrieval-Augmented Generation using external data sources
- **Deployment**: Compatible with cloud platforms like AWS, Azure, or any service that supports Flask and Gunicorn
- **Testing**: Pytest for unit testing to ensure the reliability of the application


---

## 📚 Usage

### Prerequisites

- Python 3.8+
- Flask
- LangChain
- GPT-4o mini API key

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VictorCabrejos/Neuropain-Clinical-Doc-AI.git
   cd Neuropain-Clinical-Doc-AI
   ```

2. **Set up the Environment**:
   ```bash
   python -m venv grossinger_llm
   source grossinger_llm/bin/activate  # On Windows: grossinger_llm\Scriptsctivate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**:
   - Create a `.env` file in the root directory and add your API key.
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the Application**:
   ```bash
   flask run
   ```

### Running Tests

To ensure everything is working correctly, you can run the test suite:

```bash
pytest
```

---

## 🛠️ Project Structure

```plaintext
Neuropain-Clinical-Doc-AI/
├── app/
│   ├── __init__.py            # Initializes Flask app
│   ├── langchain_pipeline.py  # Logic for interacting with GPT-4o mini
│   ├── routes.py              # API routes definitions
│   └── templates/             # HTML templates (if needed)
├── docs/
│   ├── Documento_de_Casos_de_Prueba.md # Test cases documentation
├── tests/
│   ├── test_routes.py         # Unit tests for API routes
├── .gitignore
├── config.py
├── main.py                    # Entry point for the application
└── README.md                  # Project overview and instructions
```

---

## 💡 Why This Project Matters

In the rapidly evolving field of healthcare, efficiency and accuracy are paramount. This project exemplifies how Generative AI can transform routine processes, such as clinical documentation, making them faster, more reliable, and less prone to human error. For developers and engineers, this project serves as a model for integrating AI into practical applications, showcasing how software engineering can directly contribute to improved healthcare outcomes.

---

## 👤 About the Author

**Victor Manuel Cabrejos Jr.** is a seasoned software engineer with a passion for artificial intelligence and its applications in real-world scenarios. With a background in both software development and AI, Victor specializes in creating innovative solutions that bridge the gap between cutting-edge technology and practical needs.

- **LinkedIn**: [https://www.linkedin.com/in/victorcabrejos/](https://www.linkedin.com/in/victorcabrejos/)
- **Facebook**: [https://www.facebook.com/pythonfordatascience](https://www.facebook.com/pythonfordatascience)

---

## 🌐 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For more information or inquiries, please reach out via [LinkedIn](https://www.linkedin.com/in/victorcabrejos/) or [Facebook](https://www.facebook.com/pythonfordatascience).

---

### Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find a bug or have a feature request.
