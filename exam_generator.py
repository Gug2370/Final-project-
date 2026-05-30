# Import random module
import random


# Function to load questions and answers
def load_questions(file_name):

    # Open file in read mode
    infile = open(
        file_name,
        'r',
        encoding='utf-8'
    )

    # Empty list
    lines = []

    # Read file line by line
    for line in infile:

        # Remove spaces and new lines
        line = line.strip()

        # Ignore empty lines
        if line != '':

            lines.append(line)

    # Close file
    infile.close()

    # Check if file format is correct
    if len(lines) % 2 != 0:

        raise ValueError(
            'The question bank file '
            'format is incorrect.'
        )

    # Empty list
    qa_list = []

    # Starting index
    index = 0

    # Loop through lines
    while index < len(lines):

        # Get question and answer
        question = lines[index]
        answer = lines[index + 1]

        # Store question-answer pair
        qa_list.append([question, answer])

        # Move to next pair
        index += 2

    # Return question list
    return qa_list


# Function to create exam file
def create_exam(
        qa_list,
        number_of_questions,
        output_file):

    # Open output file
    outfile = open(
        output_file,
        'w',
        encoding='utf-8'
    )

    # List to store used indexes
    used_indexes = []

    # Counter variable
    count = 1

    # Loop to write questions
    while count <= number_of_questions:

        # Generate random index
        random_index = random.randint(
            0,
            len(qa_list) - 1
        )

        # Avoid duplicate questions
        while random_index in used_indexes:

            random_index = random.randint(
                0,
                len(qa_list) - 1
            )

        # Save used index
        used_indexes.append(random_index)

        # Get question and answer
        question = qa_list[random_index][0]
        answer = qa_list[random_index][1]

        # Write question
        outfile.write(
            f'Question {count}: '
            f'{question}\n'
        )

        # Write answer
        outfile.write(
            f'Answer: {answer}\n\n'
        )

        # Increase counter
        count += 1

    # Close output file
    outfile.close()