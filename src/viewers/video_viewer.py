from PySide6.QtWidgets import QWidget, QVBoxLayout,QPushButton
from PySide6.QtMultimedia import QMediaPlayer, QCamera,QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtMultimediaWidgets import QVideoWidget
from src.viewers.explorer_function import view_cleaer

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
            

def display_vidoe_content(context,vieo_path):
    video_viewer = VideoViewer()
    video_viewer.player.setSource(QUrl(vieo_path))
    video_viewer.show()
    #video_viewer.player.play()

    play_btn = QPushButton("|> / ||")
    restart_btn = QPushButton("|_|")
    mute_btn = QPushButton("Mute")
    play_btn.clicked.connect(video_viewer.pause_play_vide)
    restart_btn.clicked.connect(video_viewer.restart_video)
    mute_btn.clicked.connect(video_viewer.mute_vide)

    layout = context.ui.reportsPage.layout()
    view_cleaer(layout,context)
    layout.addWidget(play_btn)
    layout.addWidget(restart_btn)
    layout.addWidget(mute_btn)
    layout.addWidget(video_viewer)
    video_viewer.show()