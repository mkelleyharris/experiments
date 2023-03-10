'use stric';

import { getContact, OtherInfo} from './code.js'

import { assertEquals } from "https://deno.land/std@0.178.0/testing/asserts.ts";

Deno.test("get contact info", () => {
  const contact = getContact();
  assertEquals(contact, "info@sourcecell.com");
});

Deno.test("get copyright date", () => {
  const date = OtherInfo.getCopyrightDate();
  assertEquals(date, "2023");
});
