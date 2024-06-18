from automata.fa.dfa import DFA

# Define the DFA
# Accepted string ends with '11'
# Define the DFA
dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q0', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q2'}
)

# Test cases
test_strings = ['01', '011', '1101', '1001', '0001']

for string in test_strings:
    if dfa.accepts_input(string):
        print(f'String "{string}" is accepted')
    else:
        print(f'String "{string}" is not accepted')

# Stepwise processing for '011'
stepwise_result = list(dfa.read_input_stepwise('011'))
print(stepwise_result)

# Additional single input test
if dfa.accepts_input('01'):
    print('String "01" is accepted')
else:
    print('String "01" is not accepted')s