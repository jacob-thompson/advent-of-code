from func import get_lists, get_similarity_score

def main():
    left, right = get_lists()
    similarity = get_similarity_score(left, right)
    print(similarity)

if __name__ == "__main__":
    main()