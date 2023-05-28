#!/usr/bin/env python3
import sys
import sqlite3


def add_agent(conn, aid, name):
	pass # write code here, don't forget to commit results once you execute the insert
	try:
		cursor = conn.cursor()
		cursor.execute('insert into Agent (id, name) values (?,?)',(aid, name))
		conn.commit()
		cursor.close()
		print("Scuccessful insert")
	except sqlite3.Error as e:
		print("error:", e)


def delete_agent(conn, aid):
	pass # write code here, don't forget to commit results once you execute the insert
	try:
		cursor = conn.cursor()
		cursor.execute('delete from Agent where id = ?', (aid,))
		conn.commit()
		cursor.close()
		print("Successful delete")
	except sqlite3.Error as e:
		print("error:", e)


def read_database(conn):
	agents = []

	# output should be a list of pairs agents = [(id1, name1), (id2, name2), (id3, name3), ...] ordered by id
	# write code here
	try:
		cursor = conn.cursor()
		cursor.execute('select * from Agent order by id')
		data = cursor.fetchall()
		for filed  in data:
			agent_id , agent_name = filed
			agents.append((agent_id, agent_name))
		cursor.close()
	except sqlite3.Error as e:
		print("error", e)
	return agents


def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	while True:
		agents = read_database(conn)
		print('\nActive agents:\n')
		for agent in agents:
			print(agent[0], agent[1])
		print()
		command = input('What would you like to do: [a]dd, [r]emove, or [q]uit? ')

		if command[0].startswith('a'):
			aid = input('id? ')
			name = input('name? ')
			add_agent(conn, aid, name)
			pass
		elif command[0].startswith('r'):
			aid = input('id? ')
			delete_agent(conn, aid)
			pass
		elif command[0].startswith('q'):
			break
	

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
