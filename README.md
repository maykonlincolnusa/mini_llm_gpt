# Mini LLM Chat – Projeto de IA em Python

Este projeto é um **chat inteligente simples**, desenvolvido em Python, com foco em **arquitetura de IA, organização de código e viabilidade em máquinas com poucos recursos**.

O objetivo não é competir com grandes LLMs, mas demonstrar **fundamentos reais de Inteligência Artificial, Machine Learning, segurança e engenharia de software**, sendo ideal para **portfólio profissional**.

---

## 🧠 O que este projeto faz

- Interface de chat usando **Streamlit**
- Motor de respostas com **Machine Learning**
- Modelo treinado localmente (sem APIs pagas)
- Arquitetura modular (ML, segurança, chat e app)
- Preparado para evoluir para RAG, bancos de dados e LLMs maiores

---

## 🏗️ Arquitetura do Projeto

mini_llm/
│
├── app.py # Interface principal (Streamlit)
├── chat_engine.py # Lógica do chat
│
├── ml/
│ ├── train.py # Treinamento do modelo
│ ├── inference.py # Inferência (respostas)
│ └── model.pkl # Modelo treinado
│
├── security/
│ ├── security.py # Hash e proteção de dados
│ └── crypto.py # Criptografia básica
│
├── database/ # (Pronto para uso futuro)
│
└── README.md


---

## 🤖 Inteligência Artificial utilizada

O projeto utiliza:

- **TF-IDF (Text Vectorization)**
- **Machine Learning clássico com scikit-learn**
- Inferência local em CPU
- Zero dependência de GPU
- Zero custo financeiro

Isso permite:
- Execução em computadores antigos
- Treinamento rápido
- Fácil explicação técnica (ideal para entrevistas)

---

## 🚀 Como rodar o projeto

### 1️⃣ Criar o ambiente (opcional, mas recomendado)
```bash
conda create -n mini_llm python=3.10
conda activate mini_llm

🔐 Segurança

O projeto possui uma camada inicial de segurança com:

Hash de texto

Criptografia simples

Estrutura preparada para:

Tokens

Autenticação

Proteção de dados sensíveis

🧩 Próximas evoluções (roadmap)

 Conectar banco de dados (SQLite / PostgreSQL)

 Implementar RAG (Retrieval-Augmented Generation)

 Melhorar o motor de respostas

 Integrar modelos maiores (BERT / LLMs)

 Criar assistentes especializados (ex: saúde, negócios)

📌 Objetivo do projeto

Este projeto foi criado para:

Demonstrar domínio prático de IA

Mostrar capacidade de resolver problemas reais

Servir como base para sistemas inteligentes maiores

Evoluir para aplicações comerciais no futuro

👤 Autor

Maykon Lincoln
Engenharia de Dados • Inteligência Artificial • Machine Learning e sistemas