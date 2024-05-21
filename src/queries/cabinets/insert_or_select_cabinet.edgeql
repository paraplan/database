insert Cabinet {
  name := <str>$name,
  room := <str>$room
} unless conflict on .room else Cabinet;
