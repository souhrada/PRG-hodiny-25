extends Node

var score := 0
var game_time := 0.0

@onready var score_label: Label = $Score_label
@onready var time_label: Label = $Time_label

func _process(delta):
	game_time += delta
	time_label.text = "Time: " + str(snapped(game_time, 0.1))            

func add_point():
	score += 1
	print(score)
	score_label.text = "Coins: " + str(score)
