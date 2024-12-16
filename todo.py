class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Tâche ajoutée : {task}')

    def view_tasks(self):
        if not self.tasks:
            print("Aucune tâche à afficher.")
        else:
            print("\nListe des tâches :")
            for i, t in enumerate(self.tasks, 1):
                status = "Terminée" if t["completed"] else "En cours"
                print(f'{i}. {t["task"]} [{status}]')

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f'Tâche "{self.tasks[task_index]["task"]}" marquée comme terminée.')
        else:
            print("Index de tâche invalide.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f'Tâche supprimée : {removed_task["task"]}')
        else:
            print("Index de tâche invalide.")

# Exemple d'utilisation
if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\nMenu :")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")

        choix = input("Choisissez une option : ")
        if choix == "1":
            tâche = input("Entrez la tâche : ")
            todo.add_task(tâche)
        elif choix == "2":
            todo.view_tasks()
        elif choix == "3":
            index = int(input("Entrez l'index de la tâche à marquer comme terminée : ")) - 1
            todo.complete_task(index)
        elif choix == "4":
            index = int(input("Entrez l'index de la tâche à supprimer : ")) - 1
            todo.delete_task(index)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")
