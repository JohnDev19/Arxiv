const axios = require('axios');
const { parseStringPromise } = require('xml2js');

/**
 * Searches ArXiv for articles based on the provided query.
 * @param {string} query - The search query.
 * @returns {Array} - An array of objects containing article information.
 */
async function searchArXiv(query) {
  try {
    const apiUrl = `https://export.arxiv.org/api/query?search_query=${encodeURIComponent(query)}`;
    const response = await axios.get(apiUrl);
    const xmlData = response.data;

    const parsedData = await parseStringPromise(xmlData, { explicitArray: false });
    return parsedData.feed.entry.map(entry => ({
      title: entry.title,
      id: entry.id,
      published: entry.published,
      summary: entry.summary,
      link: entry.link,
    }));
  } catch (error) {
    throw new Error(`Error while fetching ArXiv data: ${error.message}`);
  }
}

module.exports = {
  searchArXiv,
};
