import { browser } from '$app/environment';

export function formatNumberToDollar(num: string | number) {
	const moneyFormater = new Intl.NumberFormat('en-CA', {
		style: 'currency',
		currency: 'CAD'
	});

	return moneyFormater.format(Number(num));
}

// A class to help with session storage
export class SessionStore {
	private static parsers = {
		string: (value: string) => value,
		json: (value: string) => {
			try {
				return JSON.parse(value);
			} catch (e) {
				return null;
			}
		}
	};
	public static Get(field: string, expectedType: keyof typeof SessionStore.parsers) {
		let value = null;
		console.log(field, expectedType);
		if (browser) {
			if (window.sessionStorage.getItem(field) !== null) {
				console.log(window.sessionStorage.getItem(field));
				value = SessionStore.parsers[expectedType](window.sessionStorage.getItem(field)!);
			}
		}
		return value;
	}

	public static Set(field: string, value: string) {
		if (browser) window.sessionStorage.setItem(field, value);
	}
}
