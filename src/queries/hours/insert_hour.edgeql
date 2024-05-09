insert Hour {
  sub_groups := (
    select SubGroupHour
    filter .id in array_unpack(<array<uuid>>$id)
  )
}
