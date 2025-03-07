from src.bot.bot import main_bot


def main():
    print('cest parti')
    # Donner les informations d'une offre à un bot telegram
    main_bot()
    # Puis les récupérer sous forme de liste pour les stocker dans un google sheet
    #   - Entreprise, intitulé du post, description des missions, compétences requises
    #   - Type de contrat, date de l'offre, lien vers l'offre
    # Passer les informations d'une offre à chatgpt et lui demander des informations pertinantes sur l'entreprise pour
    # répondre à cette offre

    # Demander au bot qui enverra à chatgpt un message personnalisé pour répondre à l'offre
    # Stocker le message dans la bdd

    # Demander au bot de mettre l'offre comme inintéressante et stocker dans la bdd

    # Demander au bot de mettre l'offre comme postulé avec la date si besoin

    # Pouvoir demander au bot d'afficher une offre et/ou le message pour postuler

    # Avoir un fichier google sheet toujours disponible avec toutes les informations


if __name__ == "__main__":
    main()
