from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QComboBox,
    QPushButton,
    QTextEdit,
)
from services.diagnostics_service import DiagnosticsService
class DiagnosticsPage(QWidget):

    def __init__(self):
        super().__init__()

        self.service = DiagnosticsService()

        layout = QVBoxLayout(self)
        title = QLabel("🔧 Мастер диагностики")

        self.device = QComboBox()
        self.device.addItems([
            "Хроматэк Кристалл 5000",
            
        ])
        self.module = QComboBox()
        self.module.addItems([
            "ПИД",
        ])
        self.problem = QComboBox()
        self.problem.addItems([
            "Нет поджига",
        ])
        self.button = QPushButton("Начать диагностику")
        self.button.clicked.connect(self.start_diagnostics)

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        layout.addWidget(title)

        layout.addWidget(QLabel("Прибор"))
        layout.addWidget(self.device)

        layout.addWidget(QLabel("Модуль"))
        layout.addWidget(self.module)

        layout.addWidget(QLabel("Неисправность"))
        layout.addWidget(self.problem)

        layout.addSpacing(20)

        layout.addWidget(self.button)
        layout.addWidget(self.result)

        layout.addStretch()

    def start_diagnostics(self):

        self.result.clear()

        device = self.device.currentText()
        module = self.module.currentText()
        problem = self.problem.currentText()


        data = self.service.get_steps(
            device,
            module,
            problem
        )

        if not data:
            self.result.setText("Диагностика не найдена.")
            return

        
        self.result.append("=" * 45)
        self.result.append("GC Engineer AI")
        self.result.append("=" * 45)
        self.result.append("")


        self.result.append(f"Прибор: {device}")
        self.result.append(f"Модуль: {module}")
        self.result.append(f"Неисправность: {problem}")

        self.result.append("")
        self.result.append("=== Возможные причины ===")
        self.result.append("")


        for item in data.get("possible_causes", []):
            self.result.append(f"• {item}")

        self.result.append("")
        self.result.append("=== Что проверить ===")
        self.result.append("")

        for i, item in enumerate(data.get("checks", []), start=1):
            self.result.append(f"{i}. {item}")

        self.result.append("")
        self.result.append("=== Решение ===")
        self.result.append("")

        for item in data.get("solution", []):
            self.result.append(f"✓ {item}")

        self.result.append("")
        self.result.append("=" * 45)
        self.result.append("Диагностика завершена.")

    
