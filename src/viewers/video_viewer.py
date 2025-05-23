from PySide6.QtWidgets import QPushButton,QWidget,QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtCore import QUrl,QFileInfo
from PySide6.QtMultimediaWidgets import QVideoWidget
from src.viewers.explorer_function import view_cleaer, MetaDataTableWiget
import tempfile
class VideoViewer(QVideoWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)
        self.player.setVideoOutput(self)
        self.position = 0

    def restart_video(self):
        self.player.stop()
        self.player.play()
    
    def pause_play_vide(self):
        if self.player.isPlaying():
            self.position = self.player.position()
            self.player.stop()
        else:
            self.player.play()
            self.player.setPosition(self.position)
    
    def mute_vide(self):
        self.audio_output.setMuted(not self.audio_output.isMuted())
            

def display_vidoe_content(video_bytes):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_file.write(video_bytes)
    temp_file.close()

    video_viewer = VideoViewer()
    video_url = QUrl.fromLocalFile(temp_file.name)
    video_viewer.player.setSource(video_url)
    video_viewer.show()
    #video_viewer.player.play()

    play_btn = QPushButton("|> / ||")
    restart_btn = QPushButton("|_|")
    mute_btn = QPushButton("Mute")
    play_btn.clicked.connect(video_viewer.pause_play_vide)
    restart_btn.clicked.connect(video_viewer.restart_video)
    mute_btn.clicked.connect(video_viewer.mute_vide)

    tab_content = QWidget()
    tab_layout = QVBoxLayout(tab_content)


    tab_layout.addWidget(play_btn)
    tab_layout.addWidget(restart_btn)
    tab_layout.addWidget(mute_btn)
    tab_layout.addWidget(video_viewer)
    video_viewer.show()
    return tab_content