/*
 * Copyright (C) 2014 Cloudius Systems, Ltd.
 *
 * This work is open source software, licensed under the terms of the
 * BSD license as described in the LICENSE file in the top-level directory.
 */

#ifndef DEMANGLE_HH_
#define DEMANGLE_HH_

#include <stddef.h>

#include <stddef.h>
#include <memory>

namespace osv {

bool demangle(const char *name, char *buf, size_t len);
std::unique_ptr<char> demangle(const char *name);

void lookup_name_demangled(void *addr, char *buf, size_t len);

}

#endif /* DEMANGLE_HH_ */
