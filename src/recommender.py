from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and return a list of song dictionaries with typed values."""
    import csv
    songs = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                'id':           int(row['id']),
                'title':        row['title'],
                'artist':       row['artist'],
                'genre':        row['genre'],
                'mood':         row['mood'],
                'energy':       float(row['energy']),
                'tempo_bpm':    int(row['tempo_bpm']),
                'valence':      float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness']),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Score a single song against user preferences and return (score, explanation)."""
    W_GENRE        = 2.0
    W_MOOD         = 1.0
    W_ENERGY       = 0.8
    W_ACOUSTICNESS = 0.5

    parts = []
    score = 0.0

    # Genre match
    if song['genre'] == user_prefs['genre']:
        score += W_GENRE
        parts.append(f"+{W_GENRE} genre match")
    else:
        parts.append("+0 genre match")

    # Mood match
    if song['mood'] == user_prefs['mood']:
        score += W_MOOD
        parts.append(f"+{W_MOOD} mood match")
    else:
        parts.append("+0 mood match")

    # Energy similarity
    energy_sim = round(W_ENERGY * (1 - abs(song['energy'] - user_prefs['energy'])), 3)
    score += energy_sim
    parts.append(f"+{energy_sim} energy")

    # Acousticness binary match
    song_acoustic = 1 if song['acousticness'] >= 0.5 else 0
    user_acoustic = 1 if user_prefs['likes_acoustic'] else 0
    if song_acoustic == user_acoustic:
        score += W_ACOUSTICNESS
        parts.append(f"+{W_ACOUSTICNESS} acousticness match")
    else:
        parts.append("+0 acousticness match")

    return round(score, 3), ", ".join(parts)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs against user preferences and return the top k as (song, score, explanation) tuples."""
    results = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        results.append((song, score, explanation))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[:k]
