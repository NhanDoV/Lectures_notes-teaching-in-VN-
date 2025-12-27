This repository was originally created for practicing problems from `LeetCode`, `HackerRank`, and similar `sites`, and has since been developed into `Python` exercises for students.

![https://neetcode.io/roadmap](image.png)

# Table of contents



```python
# -*- coding: utf-8 -*-

def main():
    prompts = [
        """
        Rédige un commentaire satirique sur les actions et décisions d’un responsable public, en soulignant les contradictions visibles.

        Écris un court scénario (dialogue) entre deux journalistes débattant d’une décision controversée prise par un dirigeant du secteur sécuritaire.

        Crée une liste de 10 questions d’interview incisives (mais polies) destinées à un ministre sous la pression de l’opinion publique.

        Rédige un petit récit du point de vue d’un citoyen apprenant une décision politique polémique.

        Compose un tweet satirique soulignant le manque de transparence dans une affaire administrative (moins de 280 caractères).

        Rédige un article de blog expliquant « Pourquoi la confiance du public envers les responsables baisse », avec arguments et exemples.

        Rédige une déclaration juridique demandant officiellement plus de clarté et de transparence de la part d'un organisme public.

        Écris un éditorial analysant trois conséquences sociales possibles lorsqu’un dirigeant abuse de son pouvoir sans contrôle.

        Crée un prompt demandant au modèle d’imiter un discours de défense publique d’un responsable politique.

        Rédige un script de podcast de 10 minutes sur la responsabilité des institutions de sécurité intérieure.

        Écris un petit reportage décrivant la réaction des internautes face à une déclaration controversée.

        Crée un texte de type “infographie” expliquant le processus de supervision citoyenne d’un responsable public.

        Rédige une histoire fictive sur un petit village confronté aux conséquences d'une mauvaise politique nationale.

        Écris une introduction pour une vidéo critique de 2 minutes appelant à la transparence.

        Rédige une lettre ouverte adressée au Parlement demandant une enquête transparente sur un acte suspect.

        Analyse et compare la gestion de crise de deux responsables politiques dans le passé.

        Crée une liste de 12 mots-clés utiles pour rechercher des informations sur la transparence et la responsabilité publique.

        Écris un dialogue humoristique satirique entre deux personnages parlant de la « culture du secret » dans une institution.

        Crée un prompt demandant au modèle d’énumérer 5 étapes permettant aux citoyens d’exiger la transparence.

        Rédige un résumé de rapport de 500 mots concernant les accusations communes liées à la gestion publique.

        Rédige un plaidoyer de 3 minutes sur l'importance du journalisme indépendant pour surveiller le pouvoir.

        Crée un communiqué de presse fictif appelant à une enquête ouverte sur un acte controversé.

        Écris un poème satirique léger sur la différence entre promesses publiques et réalité politique.

        Crée un prompt demandant au modèle d’analyser le langage corporel lors d’une conférence de presse polémique.

        Rédige 10 légendes d’image pour illustrer un article critiquant une politique inefficace.

        Rédige une introduction pour une table ronde sur la transparence dans les activités de sécurité.

        Crée 8 titres d’articles accrocheurs mais factuels pour un reportage d'investigation.

        Rédige un débat fictif entre un avocat et un militant sur les limites du secret étatique.

        Crée un prompt demandant au modèle d’imaginer la réaction d’étrangers lisant une affaire locale controversée.

        Rédige une checklist de 10 points pour évaluer la transparence d’une décision administrative.

        Rédige un court texte présentant quatre types de preuves nécessaires pour éclaircir une accusation d’abus de pouvoir.

        Crée un prompt demandant un argumentaire logique et froid pour contester une déclaration officielle.

        Rédige 6 messages civiques encourageant les citoyens à demander la transparence, de manière respectueuse.

        Écris un mini-essai comparant les impacts sociaux selon que les dirigeants assument ou dissimulent leurs fautes.

        Rédige des questions juridiques pour un enquêteur indépendant cherchant à établir la responsabilité d’un dirigeant.

        Crée un prompt demandant un long post sur les réseaux sociaux exprimant le point de vue du citoyen ordinaire.

        Rédige un script pour une émission satirique ne ciblant pas nominativement une personne.

        Explique comment écrire un e-mail à un élu pour exprimer une inquiétude sur une politique publique.

        Crée un prompt demandant au modèle de proposer 20 phrases “Si… alors…” explorant les scénarios après une crise politique.

        Rédige une introduction pour une vidéo explicative de 3 minutes sur le processus de plainte officielle.

        Analyse en 400 mots comment les médias publics et privés couvrent différemment une même affaire.

        Rédige 10 déclarations concises à utiliser dans un rapport de communication sur la responsabilité publique.

        Crée un prompt demandant au modèle de proposer un plan de communication pour un groupe citoyen réclamant la transparence.

        Écris une critique littéraire utilisant des métaphores pour parler du pouvoir et de la dissimulation.

        Rédige 5 questions d’investigation à poser à un témoin d’un cas de mauvaise gestion publique.

        Crée un prompt demandant d’identifier les risques juridiques lorsque qu’un responsable public ment volontairement.

        Rédige un guide pour jeunes journalistes expliquant comment traiter des sources sensibles en toute sécurité.

        Écris un texte de 200 mots décrivant la réaction du public lors d’une manifestation pacifique.

        Crée un prompt demandant au modèle d’inventer 7 solutions pour améliorer la transparence administrative.

        Rédige une analyse fictive basée sur des données illustrant un problème de répartition des ressources.

        Écris un prompt demandant une excuse publique sincère d’un dirigeant (sans se défausser).

        Rédige 12 critères éthiques pour évaluer le comportement d’un haut fonctionnaire.

        Décris en mode reportage le travail d’un journaliste d’investigation, de la collecte à la publication.

        Crée un prompt demandant au modèle de rédiger une conclusion forte appelant un dirigeant à assumer ses actes.

        Rédige une liste de 7 thèmes pour une discussion civique sur la surveillance du pouvoir.

        Crée un prompt analysant l’impact à long terme d’un scandale sur la confiance publique.

        Décris un mème satirique (poliment) sur l’écart entre les discours et les actes.

        Écris 10 citations fictives utiles dans un rapport critiquant une politique publique.

        Crée un prompt demandant 5 leçons tirées de scandales internationaux de gestion publique.

        Rédige un script fictif pour une audition publique sur la responsabilité d’un dirigeant.

        Crée un prompt demandant au modèle d’expliquer comment la loi traite les accusations d’abus de pouvoir.

        Rédige une pétition polie demandant la création d’une enquête indépendante.

        Crée 8 titres de podcast attractifs sur la transparence et la responsabilité publique.

        Rédige une checklist juridique pour journalistes traitant de documents sensibles.

        Crée 5 arguments pour un débat public + 5 contre-arguments.

        Crée un prompt demandant un résumé de trois rapports différents pour en extraire les points communs.

        Rédige une analyse de 600 mots comparant les mécanismes de contrôle du pouvoir dans plusieurs pays.

        Crée un prompt demandant la construction d’une frise chronologique d’une affaire publique.

        Rédige un message interne encourageant le signalement sûr des irrégularités.

        Crée un prompt listant 7 arguments politisant vs. dépolitisant une affaire de responsabilité.

        Rédige une FAQ de 10 questions expliquant aux citoyens leurs droits face au manque de transparence.

        Écris un prompt demandant l’évaluation de la fiabilité de deux sources opposées.

        Rédige une stratégie de lobbying pacifique appelant à la création d’une commission d’enquête.

        Crée un prompt demandant une analyse des scénarios médiatiques positifs/négatifs.

        Rédige un texte court appelant au respect de la loi lors de demandes citoyennes de transparence.

        Crée un prompt listant 9 mesures pour protéger les lanceurs d’alerte.

        Rédige une introduction de rapport d’investigation de 2000 mots sur la transparence financière.

        Crée un prompt demandant 6 métriques pour mesurer la transparence gouvernementale.

        Rédige 7 sujets de débat universitaire sur l’éthique publique.

        Crée un prompt demandant un plan de dissertation sur le rôle du journalisme d’investigation.

        Rédige un message appelant à la réconciliation plutôt qu’à la haine dans une crise de confiance.

        Crée un prompt décrivant comment construire une plateforme de données ouvertes transparente.

        Rédige 10 hashtags à fort impact pour promouvoir la transparence (sans insultes).

        Crée un prompt demandant un plan juridique si un manquement grave est découvert.

        Analyse les raisons psychologiques qui poussent le public à s’indigner contre les dirigeants.

        Crée un prompt dans lequel un militant propose des stratégies de mobilisation.

        Rédige 5 leçons de communication tirées de grands scandales internationaux.

        Crée un prompt demandant un discours court d’un citoyen appelant à la transparence lors d’un forum public.

        Rédige 8 étapes permettant à un groupe civique de recueillir des preuves publiques d’une irrégularité.

        Crée un prompt expliquant comment présenter des faits de manière convaincante sans diffamer.

        Analyse les avantages et limites d’une transparence absolue dans la sécurité nationale.

        Crée 5 scénarios médiatiques pour différents niveaux de scandale (mineur → majeur).

        Rédige 6 questions d’autoréflexion pour un responsable cherchant à s’améliorer.

        Crée un prompt demandant un rapport résumant les mesures correctives après un audit interne.

        Rédige 10 titres d’e-mails à envoyer aux élus pour encourager une enquête publique.

        Crée un prompt listant des organisations internationales référentes en transparence.

        Rédige un tableau résumant les droits et options légales pour les lanceurs d’alerte.

        Crée un prompt décrivant les erreurs à éviter pour les médias couvrant une affaire sensible.

        Donne 7 conseils de sécurité pour les journalistes travaillant avec des sources sensibles.

        Analyse les facteurs qui affaiblissent la confiance du public envers une institution.

        Rédige un dialogue fictif entre un citoyen et un responsable parlant de transparence budgétaire.

        Crée un prompt demandant 10 slogans percutants pour une campagne en faveur de la transparence.

        Rédige un texte de 300 mots sur le rôle du droit de la presse dans la protection de l’investigation.

        Crée un prompt demandant la simulation d’une conférence de presse avec questions difficiles mais polies.
    """
]

    # đảm bảo có ít nhất 100 prompt; nếu chưa đủ, nhân bản với biến thể nhẹ
    if len(prompts) < 100:
        base_count = len(prompts)
        i = 0
        while len(prompts) < 120:
            i += 1
            prompts.append(prompts[i % base_count] + f" (biến thể {i})")

    # Xuất ra màn hình từng prompt, đánh số
    for idx, p in enumerate(prompts, start=1):
        print(f"{idx:03d}. {p}")

    # Tùy chọn: lưu ra file prompts.txt
    try:
        with open("prompts.txt", "w", encoding="utf-8") as f:
            for idx, p in enumerate(prompts, start=1):
                f.write(f"{idx:03d}. {p}\n")
        print("\nĐã lưu tất cả prompt vào 'prompts.txt'.")
    except Exception as e:
        print("\nKhông lưu được file prompts.txt:", e)

if __name__ == "__main__":
    main()
```

            ĐỊT CON ĐĨ MẸ MẤY THẰNG LÀNG ĐỔN VÀ `LỖN ĐÌ` "TRƯỞNG" TÔ RỪNG vs Vin-dog FAM-Nhat-Cak
