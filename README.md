# myWorker

## Creation de Database
Lors du lancement du programme, 2 databases sont créées :
- "rooms" (mongoDB)
- "users" (MySQL)

## Insérer des données dans la database
Après la création des 2 databases une questions apparaît, vous avez trois choix :
```
Which database you want to fill ? (rooms / users, or exit to leave)
```

- rooms (insérer des données dans la database rooms)
- users (insérer des données dans la database users)
- exit (quitter le programme)

Ensuite selon la base de données que vous choisissez, vous allez devoir remplir les champs demandés.
Par exemple pour la database rooms :
```
Which database you want to fill ? (rooms / users, or exit to leave)
$ rooms

Which building ? (1 or 2)
$ 1

Owner name ?
$ Perry

room added to building1 owned by Perry
```

## Supprimer les databases
Pour supprimer les databases, il suffit de lancer le programme avec l'option '-r' ou '--remove'