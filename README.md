# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python**, **Machine Learning**, and **Streamlit**. The application recommends movies similar to the one selected by the user using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Features

* 🎥 Search and select any movie from the dataset.
* 🤖 Get top movie recommendations instantly.
* 📊 Content-based recommendation using movie metadata.
* ⚡ Fast recommendation generation using precomputed similarity.
* 🖥️ Simple and interactive Streamlit web interface.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle**

---

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── app.py                  # Streamlit application
├── main.py                 # Recommendation logic
├── movies_metadata.csv     # Movie dataset
├── df.pkl                  # Processed dataframe
├── tfidf.pkl               # TF-IDF vectorizer
├── tfidf_matrix.pkl        # TF-IDF feature matrix
├── indices.pkl             # Movie index mapping
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/jpneet/movie-recommendation-system.git
```

### 2. Navigate to the project

```bash
cd movie-recommendation-system
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will start at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. Movie metadata is loaded and preprocessed.
2. Important textual features are transformed using **TF-IDF Vectorization**.
3. **Cosine Similarity** is computed between all movies.
4. When a movie is selected, the system retrieves the most similar movies based on similarity scores.
5. The top recommendations are displayed to the user.

---

## 📊 Machine Learning Concepts Used

* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Cosine Similarity
* Content-Based Recommendation System
* Feature Engineering

---

## 📸 Demo

Add screenshots of the application here.

Example:

```
assets/home.png
assets/recommendation.png
```

---

## 🔮 Future Improvements

* Movie poster integration using TMDB API
* Genre-based filtering
* Collaborative filtering
* Hybrid recommendation system
* User authentication
* Favorite movies list
* Personalized recommendations

---

## 📦 Requirements

Install all required libraries:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 👨‍💻 Author

**Japneet Singh**

* GitHub: https://github.com/jpneet
* LinkedIn: Add your LinkedIn profile here

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps others discover the project and motivates future improvements.
