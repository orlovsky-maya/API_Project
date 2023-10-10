class Checking:
    @staticmethod
    def checking_status_code(result, status_code):
        assert result.status_code == status_code, (f'Incorrect status code {result.status_code},'
                                                   f' should be {status_code}')
        print(f'Correct status code {status_code}')

    @staticmethod
    def check_json_fields(result, expected_fields):
        result_fields = result.json()
        assert list(result_fields) == expected_fields, 'Incorrect fields of json'
        print('Correct json fields')

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        result_fields = result.json()
        result_value = result_fields.get(field_name)
        assert result_value == expected_value, 'Incorrect value of field'
        print('Correct value of field')
