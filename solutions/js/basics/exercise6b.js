/* Extending BankAccount with pretty table printing */

BankAccount.prototype.printTable = function () {
    document.write("<table><thead><tr>"
        + "<th>Date</th>"
        + "<th>Transaction</th>"
        + "<th>Amount</th>"
        + "<th>Old balance</th>"
        + "<th>New balance</th>"
        + "</tr></thead>");
    for (var i = 0; i < this.log.length; i++) {
        document.write("<tr class=\"success" + this.log[i].success + "\"><td>" + this.log[i].date + "</td>"
            + "<td>" + this.log[i].transaction + "</td>"
            + "<td>" + this.log[i].amount + "</td>"
            + "<td>" + this.log[i].oldBalance + "</td>"
            + "<td>" + this.log[i].newBalance + "</td></tr>");
    }
    document.write("</table>");
}
