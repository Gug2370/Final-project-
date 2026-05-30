# Import custom module
import exam_generator


# Main function
def main():

    # Welcome message

    print(' Welcome to Professor Assistant ')

    # Ask professor name
    professor_name = input(
        'Please Enter Your Name: '
    )

    # Greeting message
    print(
        f'\nHello Professor '
        f'{professor_name}, '
        f'I am here to help you create exams.'
    )

    # Variable to continue program
    again = 'yes'

    # Loop while professor wants to continue
    while again.lower() == 'yes':

        # Ask question bank file path
        question_file = input(
            '\nEnter the path to the '
            'question bank file: '
        )

        try:

            # Load questions
            qa_list = exam_generator.load_questions(
                question_file
            )

            print(
                '\nQuestion bank loaded successfully.'
            )

            # Input validation loop
            while True:

                try:

                    # Ask number of questions
                    number = int(input(
                        'How many questions do '
                        'you want in the exam? '
                    ))

                    # Validate positive number
                    if number <= 0:

                        print(
                            'Number must be '
                            'greater than zero.'
                        )

                    # Validate available questions
                    elif number > len(qa_list):

                        print(
                            'Not enough questions '
                            'available.'
                        )

                    else:
                        break

                # Handle invalid integer
                except ValueError:

                    print(
                        'Invalid input. '
                        'Enter numbers only.'
                    )

            # Ask output file name
            output_file = input(
                'Enter output file name: '
            )

            # Create exam
            exam_generator.create_exam(
                qa_list,
                number,
                output_file
            )

            # Success message
            print(
                f'\nCongratulations Professor '
                f'{professor_name}.'
            )

            print(
                f'Your exam has been created '
                f'and saved in {output_file}'
            )

        # Handle missing file
        except FileNotFoundError:

            print('File not found.')

        # Handle invalid file format
        except ValueError as error:

            print(error)

        # Ask professor to continue
        again = input(
            '\nDo you want to create '
            'another exam? (yes/no): '
        )

    # Goodbye message
    print(
        f'\nThank you Professor '
        f'{professor_name}. '
        f'Have a good day!'
   )


# Run program
if __name__ == '__main__':
    main()