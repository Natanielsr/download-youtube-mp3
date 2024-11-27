from baixar_musicas import BaixarMusicas
from playlist import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=9tM7xr7qeho&list=RDQMXwQAo6fqxwA&start_radio=1')
list_of_urls = playlist.pegar_links_playlist()
bm = BaixarMusicas(list_of_urls)
bm.baixar_todos_videos()