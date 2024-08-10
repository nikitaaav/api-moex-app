function myFunc() {
    const tkr = document.getElementById('stock-name').value.trim();
    if (tkr) {
        fetch(`/api/stock/${tkr}`, {
            method: "GET",
            headers: { "Accept": "application/json" }
        }).then((response) => {
            return response.json();
        }).then((resp_info) => {
            const stockInfo = {
                title: tkr,
                ticker: resp_info.ticker,
                logo: resp_info.logo,
                webpage: resp_info.webpage,
                prev: resp_info.prev,
                fullname: resp_info.fullname,
                shortname: resp_info.shortname,
                market_cap: resp_info.market_cap,
                sector: resp_info.sector,
                industry: resp_info.industry
            };
            displayStockInfo(stockInfo);
        })

    }
    return false;
};

function displayStockInfo(stock) {
    document.getElementById('stock-title').textContent = stock.title;
    document.getElementById('stock-ticker').textContent = `Ticker: ${stock.ticker}`;
    document.getElementById('stock-logo').src = stock.logo;
    document.getElementById('stock-webpage').textContent = `${stock.webpage}`;
    document.getElementById('stock-webpage').href = `${stock.webpage}`;
    document.getElementById('stock-prev').textContent = `The price of the last transaction: ${stock.prev}`;
    document.getElementById('stock-fullname').textContent = `Full name: ${stock.fullname}`;
    document.getElementById('stock-shortname').textContent = `Short name: ${stock.shortname}`;
    document.getElementById('stock-info').classList.remove('hidden');
}
