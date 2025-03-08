import joblib
import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from deap import base, creator, tools, algorithms
from sklearn.metrics import accuracy_score

def train_genetic_algorithm(X_train, y_train):
    def evaluate(individual):
        rf = RandomForestClassifier(n_estimators=int(individual[0]), max_depth=int(individual[1]), random_state=42)
        rf.fit(X_train, y_train)
        preds = rf.predict(X_train)
        return accuracy_score(y_train, preds),

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_int", random.randint, 10, 200)
    toolbox.register("attr_int2", random.randint, 3, 20)
    toolbox.register("individual", tools.initCycle, creator.Individual, (toolbox.attr_int, toolbox.attr_int2), n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutPolynomialBounded, low=[10, 3], up=[200, 20], eta=1.0, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    population = toolbox.population(n=10)
    algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=10, verbose=False)
    
    best_individual = tools.selBest(population, k=1)[0]
    best_model = RandomForestClassifier(n_estimators=int(best_individual[0]), max_depth=int(best_individual[1]), random_state=42)
    best_model.fit(X_train, y_train)
    return best_model

def save_model(model, path):
    joblib.dump(model, path)

if __name__ == "__main__":
    data = pd.read_csv("data/mosquito_habitat_dataset.csv")
    X = data.drop(columns=['Habitable','Area Name'])
    y = data['Habitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    ga_model = train_genetic_algorithm(X_train, y_train)
    save_model(ga_model, "src/models/genetic_algorithm.pkl")
