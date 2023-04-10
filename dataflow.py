from graphviz import Digraph

# Create a Digraph object
dot = Digraph()

# Add nodes for each table
dot.node('Users', label='Users')
dot.node('Games', label='Games')
dot.node('GamesIntegration', label='GamesIntegration')
dot.node('Transactions', label='Transactions')
dot.node('GameLogs', label='GameLogs')
dot.node('Comps', label='Comps')
dot.node('CompPredictions', label='CompPredictions')
dot.node('Tickets', label='Tickets')
dot.node('TicketHistory', label='TicketHistory')
dot.node('Spin2Win', label='Spin2Win')

# Add edges for foreign key relationships
dot.edge('Users', 'GamesIntegration', label='UserId')
dot.edge('Users', 'Transactions', label='UserId')
dot.edge('Users', 'GameLogs', label='UserId')
dot.edge('Users', 'Comps', label='UserId')
dot.edge('Users', 'CompPredictions', label='PlayerId')
dot.edge('Users', 'Tickets', label='UserId')
dot.edge('Users', 'Spin2Win', label='PlayerId')
dot.edge('Games', 'GamesIntegration', label='GameId')
dot.edge('Games', 'GameLogs', label='GameId')
dot.edge('Games', 'CompPredictions', label='GameId')
dot.edge('Tickets', 'TicketHistory', label='TicketId')

# Render the data flow diagram
dot.render('dataflow_diagram.gv', view=True)
