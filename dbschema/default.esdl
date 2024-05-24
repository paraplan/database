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
		required sub_group: int16;
		cabinet: Cabinet;
		required occupation: str;

		constraint exclusive on ((.cabinet, .occupation, .sub_group));
	}

	type Cabinet {
		required number: str { constraint exclusive };
		required details: str;
	}
}
