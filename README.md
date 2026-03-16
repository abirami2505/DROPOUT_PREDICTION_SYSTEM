# Student Dropout Prediction System

A machine learning-powered web application that predicts student dropout risk using a Random Forest classifier. The system helps educational counselors identify at-risk students early and take preventive measures.

## 🎯 Features

- **Dropout Risk Prediction**: Predict whether a student is at high, medium, or low risk of dropping out
- **User Authentication**: Counselor signup and login functionality
- **Student Profile Management**: Upload and analyze student data
- **Dashboard**: Visualize predictions and student analytics
- **REST API**: Programmatic access to prediction models
- **Database Integration**: MySQL backend for data persistence

## 📁 Project Structure

```
dropout_prediction_system/
├── app.py                      # Main Flask application
├── train_model.py              # Model training script
├── dataset_generator.py        # Synthetic dataset generation
├── README.md                   # Project documentation
│
├── model/
│   ├── dropout_model.py        # Model definitions and utilities
│   └── dropout_model.pkl       # Trained Random Forest model
│
├── database/
│   └── schema.sql              # MySQL database schema
│
├── dataset/
│   └── synthetic_dataset.csv   # Training dataset
│
├── templates/                  # HTML templates
│   ├── index.html              # Home page
│   ├── login.html              # Counselor login
│   ├── signup.html             # Counselor registration
│   ├── upload.html             # Student data upload
│   ├── dashboard.html          # Results dashboard
│   └── results.html            # Prediction results
│
└── static/                     # Static assets
    ├── css/
    │   └── style.css           # Stylesheet
    ├── images/                 # Image assets
    └── js/
        └── upload.js           # Frontend upload logic
```

## 🔧 Prerequisites

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## 📋 Installation

### 1. Clone or Download the Project

```bash
cd dropout_prediction_system
```

### 2. Install Dependencies

```bash
pip install flask mysql-connector-python pandas scikit-learn joblib
```

### 3. Set Up MySQL Database

Update your MySQL credentials in `app.py`:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",  # Change this
    database="dropout_system"
)
```

Create the database and tables:

```bash
mysql -u root -p < database/schema.sql
```

### 4. Train the Machine Learning Model

Generate synthetic data and train the model:

```bash
python train_model.py
```

This will create `model/dropout_model.pkl` - the trained Random Forest classifier.

## 🚀 Usage

### Start the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Workflow

1. **Sign Up**: Register as a counselor
2. **Login**: Access the system with your credentials
3. **Upload Data**: Upload student information (CSV or individual records)
4. **Get Predictions**: Receive dropout risk predictions
5. **View Dashboard**: Analyze results and student profiles

## 🤖 Model Details

### Algorithm
- **Type**: Random Forest Classifier
- **Features**: 3 student attributes
- **Output**: Dropout Risk Level (High/Medium/Low)

### Input Features

| Feature | Type | Description |
|---------|------|-------------|
| `attendance_percentage` | Numeric | Student's attendance percentage (0-100) |
| `internal_marks` | Numeric | Internal examination marks |
| `backlogs` | Numeric | Number of courses with incomplete credits |
| `family_income` | Numeric | Annual family income (in currency units) |

### Training Dataset

- **File**: `dataset/synthetic_dataset.csv`
- **Samples**: Synthetic student records
- **Target**: `dropout_risk` (High/Medium/Low)

## 📊 Database Schema

### Counsellors Table

```sql
CREATE TABLE counsellors(
    counsellor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);
```

## 🔐 Security Notes

- Store database credentials in environment variables (not in source code)
- Use encrypted passwords in production
- Implement proper authentication mechanisms
- Add input validation and SQL injection prevention

## 📝 Example API Usage

```python
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model/dropout_model.pkl')

# Create a prediction
student_data = {
    'attendance_percentage': 85,
    'internal_marks': 75,
    'backlogs': 2,
    'family_income': 50000
}

df = pd.DataFrame([student_data])
prediction = model.predict(df)
print(f"Dropout Risk: {prediction[0]}")
```

## 🛠️ Development

### File Descriptions

- **app.py**: Flask web server handling routes (home, signup, login, upload, predictions)
- **train_model.py**: Loads dataset, trains Random Forest model, saves to pickle file
- **dataset_generator.py**: Generates synthetic datasets for training and testing
- **model/dropout_model.pkl**: Serialized trained ML model

### Adding Features

To extend the model with new features:

1. Update `dataset_generator.py` to include new columns
2. Modify the feature list in `train_model.py`
3. Retrain the model: `python train_model.py`
4. Update database schema if storing new student attributes

## 🐛 Troubleshooting

### MySQL Connection Error
- Ensure MySQL server is running
- Verify credentials in `app.py`
- Check database exists: `SHOW DATABASES;`

### Model Not Found
- Run `python train_model.py` to train the model
- Check that `model/dropout_model.pkl` exists

### Port Already in Use
- Flask defaults to port 5000. Change with:
  ```bash
  python app.py --port 5001
  ```

## 📈 Future Enhancements

- [ ] Add more features (socioeconomic factors, course difficulty)
- [ ] Implement data visualization dashboard
- [ ] Add email notifications for at-risk students
- [ ] Deploy to cloud platforms (AWS, Azure, GCP)
- [ ] Implement real-time batch predictions
- [ ] Add explainability features (SHAP, LIME)

## 📄 License

Specify your license here (e.g., MIT, Apache 2.0)

## 👥 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

For questions or support, contact the development team.

---

**Last Updated**: March 2026
