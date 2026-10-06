<?php
// Przykład demonstracyjny; identyfikator nie zastępuje kontroli uprawnień.
function create_case_reference(): string
{
    return 'case_' . bin2hex(random_bytes(16));
}
