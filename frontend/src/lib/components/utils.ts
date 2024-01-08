export function formatNumberToDollar(num: string | number) {
	const moneyFormater = new Intl.NumberFormat('en-CA', {
		style: 'currency',
		currency: 'CAD'
	});

	return moneyFormater.format(Number(num));
}
