import pydot

# Create a Pydot graph
graph = pydot.Dot(graph_type='digraph', rankdir='TB')

# Add nodes for each table
users_node = pydot.Node('Users', shape='rectangle')
games_node = pydot.Node('Games', shape='rectangle')
games_integration_node = pydot.Node('GamesIntegration', shape='rectangle')
transactions_node = pydot.Node('Transactions', shape='rectangle')
game_logs_node = pydot.Node('GameLogs', shape='rectangle')
comps_node = pydot.Node('Comps', shape='rectangle')
comp_predictions_node = pydot.Node('CompPredictions', shape='rectangle')
tickets_node = pydot.Node('Tickets', shape='rectangle')
ticket_history_node = pydot.Node('TicketHistory', shape='rectangle')
spin2win_node = pydot.Node('Spin2Win', shape='rectangle')

# Add nodes to the graph
graph.add_node(users_node)
graph.add_node(games_node)
graph.add_node(games_integration_node)
graph.add_node(transactions_node)
graph.add_node(game_logs_node)
graph.add_node(comps_node)
graph.add_node(comp_predictions_node)
graph.add_node(tickets_node)
graph.add_node(ticket_history_node)
graph.add_node(spin2win_node)

# Add edges for foreign keys
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
graph.write_png('class_diagram.png')
