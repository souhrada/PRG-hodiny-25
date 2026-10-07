extends Node

var score = 0

@onready var game_timer: Timer = $Game_timer
@onready var score_label: Label = $Score_label
@onready var time_label: Label = $Time_label

func add_point():
	score += 1
	print(score)
	score_label.text = "Coins: " + str(score)
