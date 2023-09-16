import pandas as pd

def compare_dicts(guesses, solutions):

    matching_keys = [key for key in guesses if key in solutions and guesses[key] != "Review"]
    correct_count = 0
    for key in matching_keys:
        if key in solutions:

            if solutions[key] == eval(guesses[key]):
                correct_count += 1
                # print(key, solutions[key], guesses[key])
            else: 
                print(key, "sols", solutions[key], guesses[key])


    return correct_count, len(matching_keys)

# Load the CSV into a DataFrame
df1 = pd.read_csv("files/sorted/labels.csv" )

# Convert the DataFrame to a dictionary
correct_solutions = df1.set_index(df1.columns[0])[df1.columns[1]].to_dict()


df2 = pd.read_csv("results/crawler_results.csv")
our_answers = df2.set_index(df2.columns[0])[df2.columns[1]].to_dict()


matched_count, total_count = compare_dicts(our_answers, correct_solutions)
print(f"Number of correct answers: {matched_count}/{total_count}")