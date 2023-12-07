import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QComboBox,
    QLabel,
    QHBoxLayout,
    QSlider,
    QFileDialog,
)
from PyQt5.QtCore import Qt
import subprocess


class SimpleInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.current_video_format = None
        self.start_time = 0  # Updated default start time
        self.finish_time = 0  # Updated default finish time
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple Interface')
        self.resize(500, 250)

        self.load_button = QPushButton('Load')
        self.convert_button = QPushButton('Convert')

        self.load_button.clicked.connect(self.load_file_dialog)
        self.convert_button.clicked.connect(self.convert_operation)

        self.video_format_combo = QComboBox()
        self.video_format_combo.addItems(['mp4', 'mpg', 'arc', 'mp3'])
        self.video_format_combo.currentIndexChanged.connect(self.update_video_format)

        self.start_time_title = QLabel("Start Time:")
        self.start_time_label = QLabel("0 min")

        self.start_time_slider = QSlider(Qt.Horizontal)
        self.start_time_slider.setMinimum(0)
        self.start_time_slider.setMaximum(10)  # Adjusted slider maximum
        self.start_time_slider.setValue(0)  # Set default value to 0
        self.start_time_slider.setTickInterval(1)
        self.start_time_slider.setTickPosition(QSlider.TicksBelow)
        self.start_time_slider.valueChanged.connect(self.update_start_time)

        self.finish_time_title = QLabel("Finish Time:")
        self.finish_time_label = QLabel("0 min")

        self.finish_time_slider = QSlider(Qt.Horizontal)
        self.finish_time_slider.setMinimum(0)
        self.finish_time_slider.setMaximum(10)  # Adjusted slider maximum
        self.finish_time_slider.setValue(0)  # Set default value to 0
        self.finish_time_slider.setTickInterval(1)
        self.finish_time_slider.setTickPosition(QSlider.TicksBelow)
        self.finish_time_slider.valueChanged.connect(self.update_finish_time)

        self.file_name_label = QLabel("No file loaded")

        layout = QVBoxLayout()

        video_layout = QHBoxLayout()
        video_layout.addWidget(QLabel("Video Format: "))
        video_layout.addWidget(self.video_format_combo)

        start_time_layout = QHBoxLayout()
        start_time_layout.addWidget(self.start_time_title)
        start_time_layout.addWidget(self.start_time_label)
        start_time_layout.addWidget(self.start_time_slider)

        finish_time_layout = QHBoxLayout()
        finish_time_layout.addWidget(self.finish_time_title)
        finish_time_layout.addWidget(self.finish_time_label)
        finish_time_layout.addWidget(self.finish_time_slider)

        layout.addWidget(self.load_button)
        layout.addLayout(video_layout)
        layout.addLayout(start_time_layout)
        layout.addLayout(finish_time_layout)
        layout.addWidget(self.file_name_label)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)
        self.show()

    def load_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Select File')
        if file_path:
            self.file_path = file_path
            file_name = file_path.split("/")[-1]
            self.file_name_label.setText(f"Loaded file: {file_name}")
            self.set_duration_slider()

    def set_duration_slider(self):
        if self.file_path:
            try:
                duration = self.get_video_duration(self.file_path)
                duration_minutes = duration / 60
                max_slider_value = int(duration_minutes * 10)  # Convert to integer
                self.start_time_slider.setMaximum(max_slider_value)
                self.finish_time_slider.setMaximum(max_slider_value)
                self.finish_time_slider.setValue(max_slider_value)  # Set to maximum position
                self.finish_time_label.setText(f"{duration_minutes:.1f} min")
                self.start_time_slider.setValue(0)  # Set start time to default 0
                self.start_time_label.setText("0 min")
            except Exception as e:
                print(f"Error: {e}")

    def get_video_duration(self, file_path):
        try:
            cmd = [
                'ffprobe', '-i', file_path, '-show_entries', 'format=duration',
                '-v', 'quiet', '-of', 'csv=p=0'
            ]
            result = subprocess.run(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True
            )
            duration = float(result.stdout)
            return int(duration)
        except Exception as e:
            print(f"Error while getting duration: {e}")
            return 0

    def update_video_format(self, index):
        self.current_video_format = self.video_format_combo.currentText()

    def update_start_time(self):
        self.start_time = self.start_time_slider.value() / 10  # Convert slider value back to minutes
        self.start_time_label.setText(f"{self.start_time:.1f} min")

    def update_finish_time(self):
        self.finish_time = self.finish_time_slider.value() / 10  # Convert slider value back to minutes
        self.finish_time_label.setText(f"{self.finish_time:.1f} min")

    def convert_operation(self):
        if self.file_path:
            print(
                f"Convert operation triggered - File: {self.file_path}, Video format: {self.current_video_format}, "
                f"Start time: {self.start_time}, Finish time: {self.finish_time}")
        else:
            print("Please select a file.")


def run_app():
    app = QApplication(sys.argv)
    window = SimpleInterface()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
