extends Area2D

@onready var game_manager: Node = %GameManager


func _on_body_entered(body: Node2D) -> void:
	print("Coin!") # Replace with function body.
	game_manager.add_point()
	queue_free()
