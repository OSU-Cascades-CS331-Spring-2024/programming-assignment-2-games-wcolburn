1. 4x4 board

	a. What were the results of each game?

		Game 1 - Depth 5:  Minimax wins
		Game 2 - Depth 3: Minimax wins
		Game 3 - Depth 2: Minimax wins
		Game 4 - Depth 1: Minimax wins
		

	b. Did the minimax player’s moves change when the depth was limited to smaller and smaller values?

		The opening two moves were always the same. Depth 2 and 1 took several turns longer to beat me though, so somewhere it started making less profitable moves.

	c. What was the average time per move for each of the games? Comment on why there is or is not a difference.

		Game 1 - Depth 5: 0.06490636816666877
		Game 2 - Depth 3: 0.024442916666666797
		Game 3 - Depth 2: 0.018201781249999827
		Game 4 - Depth 1: 0.004291777666663628

		To the human player, there difference is not noticeable during the game. However, these results show a definite decrease in time per move as the depth decreases.



2. 8x8 board

	a. What were the results of each game?

		Game 1 - Depth 5: Minimax didn't make a move quickly enough
		Game 2 - Depth 2: Tie (surprisingly!)

	b. Did the minimax player’s moves change when the depth changed?

		N/A since game 1 was terminated.

	c. What was the average time per move for each of the games? Comment on why there is or is not a difference.

		Game 1 - Depth 5: Terminated
		Game 2 - Depth 2: 0.19243942773333156

	
	Very strong difference, since depth 5 resulted in over 10 secs of computation. Depth 2, however, wasn't noticeable.