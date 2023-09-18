from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recommendation(list_cards, similarity_threshold=0.3):
    cards = list_cards['matchedCard']

    card_skills = [s["skill"] for s in cards]
    card_combined = [' '.join(skills) for skills in card_skills]

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(card_combined)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    needed_find_card = list_cards.get("id")
    idx = 0
    for card in cards:
        if card['id'] == needed_find_card:
            break
        idx += 1

    selected_card_index = idx
    recommendations = []

    for idx, similarity in enumerate(similarity_matrix[selected_card_index]):
        if idx != selected_card_index and similarity >= similarity_threshold:
            recommendations.append(cards[idx]['id'])

    print("Рекомендации для карточки", cards[selected_card_index]['id'], ":", recommendations)
    return recommendations
