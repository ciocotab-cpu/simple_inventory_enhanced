[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange?style=for-the-badge&logo=homeassistant)](https://gitlab.com)
[![license_badge](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=mit)](https://opensource.org/licenses/MIT)
<a href="https://www.buymeacoffee.com/ciocotab" target="_blank" rel="noreferrer noopener"><img src="https://img.shields.io/badge/Donate-Buy%20me%20a%20beer-yellow?style=for-the-badge&amp;logo=buy-me-a-coffee" alt="Buy me a beer"></a>
<a href="https://www.paypal.com/myaccount/transfer/homepage/external/profile?flowContextData=mzq-R_8FOQdhsKxFCaHMvh-FQbxugbOz1hlsuniz4OpES20TJ-qm2KlvfzTtLn7OQfuXHWOHvAisKPGzJc4bSZwsv5zF2yM2hA9E8a4fC0PeSh4pVdRoVf3Ndkp1jjjSCdEt4--eyvw0sV4PbhRdSnLjtQifYLg-uNB7UBTBFnmbDPwTW154Uj5eQ_f3kLiGq1c6qh4u_pG2UmujY2c4lzw_-4ngkXLYkWMTmGf-4fi15oAwPJOdSjVrECUh8b3tX4P9Z_RI6FKVBGiBp9v7t2c9SQin4QOc6hICRaPmSl4h4X4bFphK9Heyz4O0Zs_gGiMZgL9UECNXTwYonPI4LDzKTvpVEXPHFXck7j9pta8cTtRI9bnTjTEL37G9jsZHtrM0M_NHq2lX8IhK1y_lxVnuYeFVlBwDvI6_uSzSV80kfNyscsRP6VKq-l8" target="_blank" rel="noreferrer noopener"><img src="https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal&amp;style=for-the-badge" alt="PayPal"></a>

# Simple Inventory Enhanced

This project is based on **[Simple Inventory](https://github.com/blaineventurine/simple_-_inventory)**, a custom integration for Home Assistant that manages inventories and items.

This version introduces, in particular:

- the use of a stable object ID for updates, removals, and quantity adjustments;
- the ability to have objects with the same name within the same inventory;
- the inclusion of an ID in export and import data;
- a database migration to the v4 schema, which preserves objects and their associated links.

### Backup before updating

Before installing or updating to this version, export your existing inventory from Home Assistant and keep the exported file as a backup. The JSON format is recommended. After the update, the database migration should automatically retain your existing data; only import your backup via `simple_inventory_enhanced/import` if data is missing or needs to be restored. If you are importing into an inventory that is already populated, avoid using `merge_quantities`, as this would cause quantities to be added together again. The import feature supports both JSON and CSV formats; further details can be found in the [Import and Export](#import-and-export) section.
