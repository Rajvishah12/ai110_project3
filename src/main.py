"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print("Loaded songs:", len(songs))

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False}
    # user_prefs = {"genre": "pop", "mood": "intense", "energy": 0.5, "likes_acoustic": False} # additional test 1
    # user_prefs = user_prefs = {"genre": "jazz", "mood": "moody", "energy": 0.2, "likes_acoustic": True} # additional test 2
    user_prefs = {"genre": "lofi", "mood": "relaxed", "energy": 0.2, "likes_acoustic": True} # additional test 3

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
