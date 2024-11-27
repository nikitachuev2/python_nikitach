
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Загрузка и подготовка данных
data = pd.read_csv('data.csv')  # Загрузка данных из файла data.csv
data = data.drop(columns=['filename'])  # Удаляем столбец с названием дорожки
labels = data['label'].values  # Извлекаем метки как массив
data = data.drop(columns=['label'])

# 2. Кодирование жанров
le = LabelEncoder()
labels_encoded = le.fit_transform(labels)

# 3. Нормализация признаков
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# 4. Разделение на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(data_scaled, labels_encoded, test_size=0.2, random_state=42)

# 5. Преобразование в формат PyTorch
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# 6. Определение архитектуры нейронной сети
class MusicGenreNN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(MusicGenreNN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, num_classes),  # Выходной слой
            nn.Softmax(dim=1)  # Softmax для вероятностей
        )

    def forward(self, x):
        return self.network(x)

# 7. Инициализация модели, функции потерь и оптимизатора
input_size = X_train.shape[1]
num_classes = len(le.classes_)
model = MusicGenreNN(input_size, num_classes)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 8. Обучение модели
num_epochs = 20
for epoch in range(num_epochs):
    model.train()
    for inputs, labels in train_loader:
        optimizer.zero_grad()  # Обнуление градиентов
        outputs = model(inputs)  # Прямой проход
        loss = criterion(outputs, labels)  # Вычисление потерь
        loss.backward()  # Обратный проход
        optimizer.step()  # Обновление параметров

    print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 9. Проверка точности на тестовой выборке
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f'Accuracy of the model on the test set: {accuracy:.2f}%')

# 10. Проверка предсказания на первом элементе тестовой выборки
first_input = X_test_tensor[0].unsqueeze(0)  # Добавление измерения батча
model.eval()
with torch.no_grad():
    first_output = model(first_input)
    first_prediction = torch.argmax(first_output).item()

print(f'Predicted genre for first test sample: {le.inverse_transform([first_prediction])[0]}')
print(f'Actual genre: {le.inverse_transform([y_test[0]])[0]}')
