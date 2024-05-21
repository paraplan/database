module default {
	type `Group` {
		required name: str;
		required full_name: str;
	}

	type User {
		required telegram_id: int64 { constraint exclusive };
		`group`: `Group`;
		required created_at: datetime {
			default := datetime_of_transaction();
			readonly := true
		};
	}

	type StudyDay {
		required date: datetime;
		required `group`: `Group`;
		required multi hours: Hour;
	}

	type Hour {
		required multi sub_groups: SubGroupHour;
	}

	type Cabinet {
		required room: str { constraint exclusive };
		required name: str;
	}

	type SubGroupHour {
		required occupation: str;
		required cabinet: Cabinet;
	}
}
