from baixar_musicas import BaixarMusicas
from playlist import Playlist

playlist = Playlist('[coloque_aqui_a_url_da_playlist_que_voce_deseja_baixar]')
list_of_urls = playlist.pegar_links_playlist()
bm = BaixarMusicas(list_of_urls)
bm.baixar_todos_videos()