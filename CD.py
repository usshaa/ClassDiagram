import pydot

# Create a Pydot graph
graph = pydot.Dot(graph_type='digraph', rankdir='TB')

# Define a helper function to add class nodes
def add_class_node(name, fields=None, methods=None):
    label = name
    if fields:
        label += '\n' + '\n'.join(fields)
    if methods:
        label += '\n' + '\n'.join(methods)
    node = pydot.Node(name, shape='rectangle', label=label)
    graph.add_node(node)

# Add class nodes with fields and methods
add_class_node('Users', fields=['-UserId: int', '-Username: str', '-Email: str'], methods=['+get_user_info()', '+update_user_info()'])
add_class_node('Games', fields=['-GameId: int', '-GameName: str', '-GameType: str'], methods=['+get_game_info()', '+update_game_info()'])
add_class_node('GamesIntegration', fields=['-IntegrationId: int', '-UserId: int', '-GameId: int'], methods=['+get_integration_info()', '+update_integration_info()'])
add_class_node('Transactions', fields=['-TransactionId: int', '-UserId: int', '-Amount: float'], methods=['+get_transaction_info()', '+update_transaction_info()'])
add_class_node('GameLogs', fields=['-LogId: int', '-UserId: int', '-GameId: int', '-LogMessage: str'], methods=['+get_log_info()', '+update_log_info()'])
add_class_node('Comps', fields=['-CompId: int', '-UserId: int', '-CompType: str'], methods=['+get_comp_info()', '+update_comp_info()'])
add_class_node('CompPredictions', fields=['-PredictionId: int', '-PlayerId: int', '-GameId: int', '-PredictionValue: str'], methods=['+get_prediction_info()', '+update_prediction_info()'])
add_class_node('Tickets', fields=['-TicketId: int', '-UserId: int', '-TicketType: str'], methods=['+get_ticket_info()', '+update_ticket_info()'])
add_class_node('TicketHistory', fields=['-HistoryId: int', '-TicketId: int', '-HistoryMessage: str'], methods=['+get_history_info()', '+update_history_info()'])
add_class_node('Spin2Win', fields=['-SpinId: int', '-PlayerId: int', '-SpinResult: str'], methods=['+get_spin_info()', '+update_spin_info()'])

# Add edges for relationships
graph.add_edge(pydot.Edge('Users', 'GamesIntegration', label='UserId'))
graph.add_edge(pydot.Edge('Games', 'GamesIntegration', label='GameId'))
graph.add_edge(pydot.Edge('Users', 'Transactions', label='UserId'))
graph.add_edge(pydot.Edge('Users', 'GameLogs', label='UserId'))
graph.add_edge(pydot.Edge('Games', 'GameLogs', label='GameId'))
graph.add_edge(pydot.Edge('Users', 'Comps', label='UserId'))
graph.add_edge(pydot.Edge('Users', 'CompPredictions', label='PlayerId'))
graph.add_edge(pydot.Edge('Games', 'CompPredictions', label='GameId'))
graph.add_edge(pydot.Edge('Users', 'Tickets', label='UserId'))
graph.add_edge(pydot.Edge('Tickets', 'TicketHistory', label='TicketId'))
graph.add_edge(pydot.Edge('Users', 'Spin2Win', label='PlayerId'))

# Save the diagram to a file
graph.write_png('classdg.png')
graph.write_png('classdg.svg')

